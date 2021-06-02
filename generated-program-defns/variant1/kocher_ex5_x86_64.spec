prog _generated-binaries_variant1_kocher_ex5_x86_64 {
ENTRY_4194304:
    4194304:	push	rbp;
    4194305:	mov	rbp, rsp;
    4194308:	mov	qword ptr [rbp - 8], rdi;
    4194312:	mov	rax, qword ptr [rbp - 8];
    4194316c:	cmp	rax, qword ptr [0x500000];
    4194324:	jae	0x400076;
ENTRY_4194330:
    4194330a:	mov	rax, qword ptr [rbp - 8];
    4194334e:	sub	rax, 1;
    4194340:	mov	qword ptr [rbp - 0x10], rax;
    4194344:	cmp	qword ptr [rbp - 0x10], 0;
    4194349d:	jb	0x400071;
ENTRY_4194422:
    4194422:	pop	rbp;
    4194423:	ret;
ENTRY_4194417:
    4194417:	jmp	0x400076;
ENTRY_4194355:
    4194355:	mov	rax, qword ptr [rbp - 0x10];
    4194359:	movzx	ecx, byte ptr [rax + 0x500008];
    4194367f:	shl	ecx, 9;
    4194370:	movsxd	rax, ecx;
    4194373:	movzx	ecx, byte ptr [rax + 0x500010];
    4194381d:	movzx	edx, byte ptr [0x500018];
    4194389:	and	edx, ecx;
    4194391:	mov	byte ptr [0x500018], dl;
    4194398e:	mov	rax, qword ptr [rbp - 0x10];
    4194402:	add	rax, -1;
    4194408:	mov	qword ptr [rbp - 0x10], rax;
    4194412c:	jmp	0x400028;
ENTRY_4194344:
    4194344:	cmp	qword ptr [rbp - 0x10], 0;
    4194349d:	jb	0x400071;
}
