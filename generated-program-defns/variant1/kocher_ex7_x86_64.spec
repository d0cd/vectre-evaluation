prog _generated-binaries_variant1_kocher_ex7_x86_64 {
ENTRY_4194304:
    4194304:	push	rbp;
    4194305:	mov	rbp, rsp;
    4194308:	mov	qword ptr [rbp - 8], rdi;
    4194312:	mov	rax, qword ptr [rbp - 8];
    4194316c:	cmp	rax, qword ptr [0x400068];
    4194324:	jne	0x400045;
ENTRY_4194330:
    4194330a:	mov	rax, qword ptr [rbp - 8];
    4194334e:	movzx	ecx, byte ptr [rax + 0x500000];
    4194342:	shl	ecx, 9;
    4194345:	movsxd	rax, ecx;
    4194348c:	movzx	ecx, byte ptr [rax + 0x500008];
    4194356:	movzx	edx, byte ptr [0x500010];
    4194364c:	and	edx, ecx;
    4194366e:	mov	byte ptr [0x500010], dl;
    4194373:	mov	rax, qword ptr [rbp - 8];
    4194377:	cmp	rax, qword ptr [0x500018];
    4194385:	jae	0x400063;
ENTRY_4194373:
    4194373:	mov	rax, qword ptr [rbp - 8];
    4194377:	cmp	rax, qword ptr [0x500018];
    4194385:	jae	0x400063;
ENTRY_4194391:
    4194391:	mov	rax, qword ptr [rbp - 8];
    4194395b:	mov	qword ptr [0x400068], rax;
    4194403:	pop	rbp;
    4194404:	ret;
ENTRY_4194403:
    4194403:	pop	rbp;
    4194404:	ret;
}
