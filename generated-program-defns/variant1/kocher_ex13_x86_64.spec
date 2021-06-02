prog _generated-binaries_variant1_kocher_ex13_x86_64 {
ENTRY_4194304:
    4194304:	push	rbp;
    4194305:	mov	rbp, rsp;
    4194308:	sub	rsp, 0x10;
    4194312:	mov	qword ptr [rbp - 8], rdi;
    4194316c:	mov	rdi, qword ptr [rbp - 8];
    4194320:	call	0x500000;
ENTRY_5242880:

ENTRY_4194325:
    4194325:	cmp	eax, 0;
    4194328:	je	0x400049;
ENTRY_4194377:
    4194377:	add	rsp, 0x10;
    4194381d:	pop	rbp;
    4194382e:	ret;
ENTRY_4194334:
    4194334e:	mov	rax, qword ptr [rbp - 8];
    4194338:	movzx	ecx, byte ptr [rax + 0x500008];
    4194346a:	shl	ecx, 9;
    4194349d:	movsxd	rax, ecx;
    4194352:	movzx	ecx, byte ptr [rax + 0x500010];
    4194360:	movzx	edx, byte ptr [0x500018];
    4194368:	and	edx, ecx;
    4194370:	mov	byte ptr [0x500018], dl;
    4194377:	add	rsp, 0x10;
    4194381d:	pop	rbp;
    4194382e:	ret;
}
