prog _generated-binaries_variant1_kocher_ex12_x86_64 {
ENTRY_4194304:
    4194304:	push	rbp;
    4194305:	mov	rbp, rsp;
    4194308:	mov	qword ptr [rbp - 8], rdi;
    4194312:	mov	qword ptr [rbp - 0x10], rsi;
    4194316c:	mov	rax, qword ptr [rbp - 8];
    4194320:	add	rax, qword ptr [rbp - 0x10];
    4194324:	cmp	rax, qword ptr [0x500000];
    4194332c:	jae	0x400051;
ENTRY_4194338:
    4194338:	mov	rax, qword ptr [rbp - 8];
    4194342:	add	rax, qword ptr [rbp - 0x10];
    4194346a:	movzx	ecx, byte ptr [rax + 0x500008];
    4194354:	shl	ecx, 9;
    4194357:	movsxd	rax, ecx;
    4194360:	movzx	ecx, byte ptr [rax + 0x500010];
    4194368:	movzx	edx, byte ptr [0x500018];
    4194376:	and	edx, ecx;
    4194378a:	mov	byte ptr [0x500018], dl;
    4194385:	pop	rbp;
    4194386:	ret;
ENTRY_4194385:
    4194385:	pop	rbp;
    4194386:	ret;
}
